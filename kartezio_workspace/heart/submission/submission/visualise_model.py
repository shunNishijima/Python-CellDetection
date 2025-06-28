from kartezio.easy import show_graph, load_model
from kartezio.inference import SingleModel
from kartezio.dataset import read_dataset, Dataset
from kartezio.model.components import KartezioParser, KartezioGenome
import cv2

MODEL_FILE = "models/45_images/331539-d865b1d3-1901-42f1-948e-e349665805ab/elite.json"
DATASET_FOLDER = "dataset"
OUTPUT_FOLDER = "visuals"


def main():
    model: SingleModel = load_model(MODEL_FILE)
    dataset: Dataset = read_dataset(DATASET_FOLDER, counting=True, preview=True)
    one_x = dataset.test_x[0]

    save_node_outputs(model, one_x, OUTPUT_FOLDER)
    save_model_graph(model, OUTPUT_FOLDER)

# WARNING: save_model_graph requires pygraphviz which is hard to install
def save_model_graph(model, output_directory):
    graph = show_graph(model)
    graph.draw(f"{output_directory}/model_graph.png")


def save_node_outputs(model, one_x, output_directory):
    parser: KartezioParser = model.parser
    genome: KartezioGenome = model.genome
    graph_list = parser.parse_to_graphs(genome)
    # get node outputs
    node_output_map = parser._x_to_output_map(genome, graph_list, one_x)
    # add model outputs
    prediction = model.predict([one_x])[0]
    output_start = parser.shape.out_idx
    for output_index in range(parser.shape.outputs):
        node_output_map[output_start + output_index] = prediction[output_index]["mask"]
    # save node outputs
    for index, output in node_output_map.items():
        cv2.imwrite(f"{output_directory}/node_{index}_output.png", output)


if __name__ == "__main__":
    main()

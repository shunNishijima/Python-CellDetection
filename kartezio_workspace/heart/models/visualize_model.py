import cv2
import numpy as np
from skimage.morphology import remove_small_objects, remove_small_holes, disk, erosion, dilation, opening, closing, white_tophat, black_tophat
from skimage.filters import gaussian, laplace, sobel, threshold_otsu
from scipy.ndimage import distance_transform_edt

# Mapping Kartezio functions to processing operations
function_map = {
    "max": cv2.max,
    "min": cv2.min,
    "mean": lambda x, y: (x / 2 + y / 2).astype(np.uint8),
    "add": cv2.add,
    "subtract": cv2.subtract,
    "bitwise_not": cv2.bitwise_not,
    "bitwise_or": cv2.bitwise_or,
    "bitwise_and": cv2.bitwise_and,
    "bitwise_xor": cv2.bitwise_xor,
    "bitwise_and_mask": lambda x, mask: cv2.bitwise_and(x, x, mask=mask),
    "sqrt": lambda x: cv2.sqrt(x.astype(np.float32)).astype(np.uint8),
    "pow2": lambda x: (np.power(x, 2)).astype(np.uint8),
    "exp": lambda x: (np.exp(x.astype(np.float32)) * 255 / np.exp(255)).astype(np.uint8),
    "log": lambda x: (np.log1p(x.astype(np.float32)) * 255 / np.log1p(255)).astype(np.uint8),
    "median_blur": lambda x, k=3: np.median(x, disk(k)),
    "gaussian_blur": lambda x, sigma=1: (gaussian(x, sigma=sigma) * 255).astype(np.uint8),
    "laplacian": lambda x: (laplace(x.astype(np.float32)) * 255).astype(np.uint8),
    "sobel": lambda x: sobel(x).astype(np.uint8),
    "robert_cross": lambda x: cv2.filter2D(x, -1, np.array([[1, 0], [0, -1]], dtype=np.int8)),
    "canny": lambda x, p1, p2: cv2.Canny(x, p1, p2),
    "sharpen": lambda x: cv2.filter2D(x, -1, np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)),
    "gabor": lambda x, ksize=21, sigma=5, theta=np.pi/4, lambd=np.pi/4, gamma=0.5: cv2.filter2D(
        x, cv2.CV_32F, cv2.getGaborKernel((ksize, ksize), sigma, theta, lambd, gamma, 0, ktype=cv2.CV_32F)),
    "abs_diff": cv2.absdiff,
    "abs_diff2": lambda x, y: cv2.absdiff(x, y),
    "fluo_tophat": lambda x: white_tophat(x, disk(3)),
    "rel_diff": lambda x, y: cv2.divide(cv2.absdiff(x, y), cv2.add(x, y), scale=255),
    "erode": lambda x, k=3: erosion(x, disk(k)),
    "dilate": lambda x, k=3: dilation(x, disk(k)),
    "open": lambda x, k=3: opening(x, disk(k)),
    "close": lambda x, k=3: closing(x, disk(k)),
    "morph_gradient": lambda x, k=3: dilation(x, disk(k)) - erosion(x, disk(k)),
    "morph_tophat": lambda x: white_tophat(x, disk(3)),
    "morph_blackhat": lambda x: black_tophat(x, disk(3)),
    "fill_holes": lambda x: (x > threshold_otsu(x)).astype(np.uint8),
    "remove_small_objects": lambda x, min_size=64: remove_small_objects(x > 0, min_size=min_size).astype(np.uint8),
    "remove_small_holes": lambda x, area_threshold=64: remove_small_holes(x > 0, area_threshold=area_threshold).astype(np.uint8),
    "threshold": lambda x, t=128: (x > t).astype(np.uint8) * 255,
    "threshold_at_1": lambda x: (x > 1).astype(np.uint8) * 255,
    "distance_transform": lambda x: distance_transform_edt(x > 0).astype(np.uint8),
    "distance_transform_and_thresh": lambda x, thresh=5: (distance_transform_edt(x > 0) > thresh).astype(np.uint8) * 255,
    "inrange_bin": lambda x, low, high: cv2.inRange(x, low, high),
    "inrange": lambda x, low, high: cv2.inRange(x, low, high)
}

# Example sequence and function list
sequence = [[0, 0, 0, 0, 0], [38, 0, 0, 44, 189], [15, 0, 0, 147, 113], [40, 1, 1, 200, 23], [40, 0, 1, 92, 183], [41, 0, 1, 72, 53], [16, 2, 3, 233, 128], [20, 2, 5, 178, 234], [39, 7, 1, 177, 77], [29, 4, 3, 226, 197], [12, 6, 3, 123, 224], [8, 2, 6, 120, 129], [36, 3, 0, 100, 251], [11, 6, 9, 158, 207], [18, 6, 0, 224, 181], [1, 8, 4, 222, 243], [0, 3, 9, 25, 17], [26, 11, 1, 233, 182], [6, 2, 13, 3, 235], [28, 15, 3, 153, 23], [40, 2, 2, 98, 238], [5, 19, 8, 108, 60], [9, 7, 11, 26, 12], [3, 14, 2, 180, 131], [11, 11, 2, 246, 110], [1, 11, 2, 84, 205], [23, 14, 19, 62, 226], [15, 14, 18, 25, 171], [5, 27, 0, 198, 60], [4, 8, 0, 114, 113], [19, 29, 4, 181, 230], [0, 19, 0, 0, 0]]  # shortened example
functions = ["max", "min", "mean", "add", "subtract", "bitwise_not", "bitwise_or", "bitwise_and","bitwise_and_mask",
            "bitwise_xor","sqrt","pow2","exp","log","median_blur","gaussian_blur","laplacian","sobel","robert_cross",
            "canny","sharpen","gabor","abs_diff","abs_diff2","fluo_tophat","rel_diff","erode","dilate","open",
            "close","morph_gradient","morph_tophat","morph_blackhat","fill_holes","remove_small_objects",
            "remove_small_holes","threshold","threshold_at_1","distance_transform","distance_transform_and_thresh",
            "inrange_bin","inrange"]

# Path to your single image file
image_path = "C:/Module9/Project/module9-dsai/kartezio_workspace/heart/ex_data/images/la_011_pos_77.png"  # replace with the actual path
# Load the image
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Load in grayscale; use cv2.IMREAD_COLOR for color
results = []

# Load or initialize images array
image_path = "C:/Module9/Project/module9-dsai/kartezio_workspace/heart/ex_data/images/la_011_pos_77.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    raise ValueError(f"Image at {image_path} could not be loaded.")
images = [image] * 10  # Placeholder images list, repeated single image for testing

# Processing each node based on the sequence and function map
results = []
for idx, node in enumerate(sequence):
    func_idx, input_1_idx, input_2_idx, param1, param2 = node
    func_name = functions[func_idx]

    # Fetch inputs based on indices
    input_1 = images[input_1_idx]
    input_2 = images[input_2_idx] if input_2_idx < len(images) else None
    func = function_map.get(func_name)

    # Apply function and save result if valid
    if func and input_2 is not None:
        result = func(input_1, input_2)
    elif func:
        result = func(input_1)

    # Save intermediate result
    results.append(result)
    cv2.imwrite(f"intermediate_result_{idx}.png", result)
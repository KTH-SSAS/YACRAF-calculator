LENGTH_UNIT = 25
LENGTH_UNIT_ZOOM_LIMITS = (5, 50)

SYMBOL_VALUE_TYPE_NUMBER = "N"
SYMBOL_VALUE_TYPE_TRIANGLE = "T"
ACTIVE_VALUE_TYPE_SYMBOLS_CONFIGS = [(SYMBOL_VALUE_TYPE_NUMBER, "Number (integer or float)"), (SYMBOL_VALUE_TYPE_TRIANGLE, "Triangle distribution (a / b / c)")]

SYMBOL_CALCULATION_TYPE_MEAN = "M"
SYMBOL_CALCULATION_TYPE_AND = "&"
SYMBOL_CALCULATION_TYPE_OR = "|"
SYMBOL_CALCULATION_TYPE_MULTIPLICATION = "*"
SYMBOL_CALCULATION_TYPE_TRIANGLE = "T"
ACTIVE_CALCULATION_TYPE_SYMBOLS_CONFIGS = [(SYMBOL_CALCULATION_TYPE_MEAN, "Mean of inputs"), (SYMBOL_CALCULATION_TYPE_AND, "AND (addition) of inputs"), (SYMBOL_CALCULATION_TYPE_OR, "OR (maximum) of inputs"), (SYMBOL_CALCULATION_TYPE_MULTIPLICATION, "Multiplication of input values"), (SYMBOL_CALCULATION_TYPE_TRIANGLE, "Sample two triangle distributions - ratio of input (1) > (2)")]

SAMPLES_TRIANGLE_DISTRIBUTION = 1000
ENUMERATED_INPUT_CALCULATION_TYPE_SYMBOLS = [SYMBOL_CALCULATION_TYPE_TRIANGLE]

SAVES_PATH = "saved_views"
FILE_PATHS_SAVES_PATH = f"{SAVES_PATH}/view_file_paths.csv"
CONFIGURATION_SAVES_PATH = f"{SAVES_PATH}/configurations"
SETUP_SAVES_PATH = f"{SAVES_PATH}/setups"

FONT = ("Arial", 11)

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 700
BACKGROUND_COLOR = "white"
GUI_BLOCK_START_COORDINATES = ((10, 10), (12, 12))

SAVE_WIDTH = 4
SAVE_HEIGHT = 1
SAVE_COLOR = "cyan"
SHOULD_RESTORE_SAVE = True
SAVE_POSITION = (0, CANVAS_HEIGHT // LENGTH_UNIT - SAVE_HEIGHT)

CHANGE_VIEW_WIDTH = 5
CHANGE_VIEW_HEIGHT = 1
CHANGE_VIEW_COLOR = "orange"
CHANGE_VIEW_SELECTED_COLOR = "cyan"
CHANGE_VIEW_CONFIGURATION_START_POSITION = (CANVAS_WIDTH // LENGTH_UNIT - 2 * CHANGE_VIEW_WIDTH, 0)
CHANGE_VIEW_SETUP_START_POSITION = (CANVAS_WIDTH // LENGTH_UNIT - CHANGE_VIEW_WIDTH, 0)

ADD_CLASS_WIDTH = 5
ADD_CLASS_HEIGHT = 1
ADD_CLASS_COLOR = "green"

ADD_TO_SETUP_WIDTH = ADD_CLASS_WIDTH
ADD_TO_SETUP_HEIGHT = ADD_CLASS_HEIGHT
ADD_TO_SETUP_COLOR = ADD_CLASS_COLOR

ADD_INPUT_WIDTH = ADD_CLASS_WIDTH
ADD_INPUT_HEIGHT = ADD_CLASS_HEIGHT
ADD_INPUT_COLOR = ADD_CLASS_COLOR

CALCULATE_VALUES_WIDTH = ADD_CLASS_WIDTH
CALCULATE_VALUES_HEIGHT = ADD_CLASS_HEIGHT
CALCULATE_VALUES_COLOR = "cyan"
CALCULATE_VALUES_POSITION = (CANVAS_WIDTH / (2 * LENGTH_UNIT), 0)

ADD_CONNECTION_WIDTH = ADD_CLASS_WIDTH
ADD_CONNECTION_HEIGHT = ADD_CLASS_HEIGHT
ADD_CONNECTION_COLOR = "cyan"
ADD_CONNECTION_POSITION = (CANVAS_WIDTH / (2 * LENGTH_UNIT) - ADD_CONNECTION_WIDTH, 0)

CLASS_WIDTH = 5
CLASS_HEIGHT = 1
CLASS_COLOR = "gray"

ATTRIBUTE_WIDTH = CLASS_WIDTH
ATTRIBUTE_HEIGHT = CLASS_HEIGHT
ATTRIBUTE_TEXT_OFFSET = 5
ATTRIBUTE_COLOR = "lightgray"

DISTRIBUTION_WIDTH = CLASS_HEIGHT
DISTRIBUTION_HEIGHT = CLASS_HEIGHT
DISTRIBUTION_COLOR = "orange"

ADD_ATTRIBUTE_WIDTH = CLASS_HEIGHT
ADD_ATTRIBUTE_HEIGHT = CLASS_HEIGHT
ADD_ATTRIBUTE_COLOR = "green"

ADD_CHANGE_VIEW_WIDTH = ADD_ATTRIBUTE_WIDTH
ADD_CHANGE_VIEW_HEIGHT = ADD_ATTRIBUTE_HEIGHT
ADD_CHANGE_VIEW_COLOR = ADD_ATTRIBUTE_COLOR

INPUT_WIDTH = CLASS_HEIGHT
INPUT_HEIGHT = CLASS_HEIGHT
INPUT_COLOR = "orange"

CONNECTION_END_WIDTH = CLASS_HEIGHT
CONNECTION_END_HEIGHT = CLASS_HEIGHT
CONNECTION_END_COLOR = "black"

CORNER_WIDTH = CLASS_HEIGHT / 4
CORNER_HEIGHT = CLASS_HEIGHT / 4
CORNER_COLOR = "black"
CONNECTION_DASH = (5, 2)

NUM_ORDER_CIRCLE_RADIUS = ATTRIBUTE_HEIGHT / 3
NUM_ORDER_CIRCLE_OUTLINE = 2
NUM_ORDER_CIRCLE_COLOR = "orange"
NUM_ORDER_CIRCLE_OUTLINE_COLOR = "black"

LINKED_GROUP_CIRCLE_RADIUS = NUM_ORDER_CIRCLE_RADIUS
LINKED_GROUP_CIRCLE_OUTLINE = NUM_ORDER_CIRCLE_OUTLINE
LINKED_GROUP_CIRCLE_COLOR = "cyan"
LINKED_GROUP_CIRCLE_OUTLINE_COLOR = "black"

SETUP_WIDTH_MULTIPLIER = 2

OUTLINE_WIDTH = 1
OUTLINE_COLOR = "black"

CONNECTION_WIDTH = 2
CONNECTION_COLOR = "black"

OPTION_FIELDS_PADDING = 5
OPTION_RADIO_BUTTON_CONFIGURATION_ATTRIBUTE_WIDTH = 10
OPTION_RADIO_BUTTON_CONFIGURATION_INPUT_WIDTH = 50

MOUSE_PRESS = "MOUSE_PRESSABLE"
MOUSE_DRAG = "MOUSE_DRAGGABLE"

MOUSE_LEFT_PRESS = "<ButtonPress-1>"
MOUSE_LEFT_DRAG = "<B1-Motion>"
MOUSE_LEFT_RELEASE = "<ButtonRelease-1>"
MOUSE_RIGHT_PRESS = "<ButtonPress-3>"
MOUSE_MOTION = "<Motion>"
MOUSE_WHEEL = "<MouseWheel>"
MOUSE_WHEEL_UP = "<Button-4>"
MOUSE_WHEEL_DOWN = "<Button-5>"

from genai_stack.genai_server.settings.config import read_configurations
from genai_stack.genai_server.utils import get_current_stack

path = "${directory_path}"

server_configurations, stack_configurations = read_configurations(path)

stack = get_current_stack(config=stack_configurations)

stack.run_server(host="${host}", port=${port})
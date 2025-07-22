from google.genai import types

from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.run_python import schema_run_python_file, run_python_file
from functions.write_file_content import schema_write_file, write_file

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

def call_function(function_call_part, verbose=False):
    working_dir = "./calculator"
    if function_call_part.name == "get_files_info":
        result = get_files_info(working_dir, **function_call_part.args)
    elif function_call_part.name == "get_file_content":
        result = get_file_content(working_dir, **function_call_part.args)
    elif function_call_part.name == "run_python_file":
        result = run_python_file(working_dir, **function_call_part.args)
    elif function_call_part.name == "write_file":
        result = write_file(working_dir, **function_call_part.args)
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": result},
            )
        ],
    )

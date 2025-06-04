import json
import os
from pathlib import Path


def format_parameter(param):
    """Format a single parameter for the docstring."""
    param_str = f"{param['name']} : {param['type']}"
    if param.get('optional', False):
        param_str += ", optional"
    return param_str


def create_docstring(api_data):
    """Create a docstring from API data."""
    lines = []
    
    # Description
    lines.append(api_data.get('description', 'No description available.'))
    lines.append("")
    
    # Parameters
    if 'Parameters' in api_data and api_data['Parameters']:
        lines.append("Parameters:")
        lines.append("-----------")
        for param in api_data['Parameters']:
            param_line = format_parameter(param)
            lines.append(f"{param_line}")
            if 'description' in param:
                lines.append(f"    {param['description']}")
    
    # Returns
    if 'Returns' in api_data:
        lines.append("")
        lines.append("Returns:")
        lines.append("--------")
        returns = api_data['Returns']
        if isinstance(returns, dict):
            lines.append(f"{returns.get('type', 'Unknown')}")
            if 'description' in returns:
                lines.append(f"    {returns['description']}")
    
    # Examples
    if 'example' in api_data:
        lines.append("")
        lines.append("Examples:")
        lines.append("--------")
        lines.append(f">>> {api_data['example']}")
    
    # Join with newlines and return as single-line string with \n
    return "\n".join(lines)


def process_module_json(json_path):
    """Process a single module JSON file and add Docstring fields."""
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    # Process each module in the JSON
    for module_name, module_data in data.items():
        if isinstance(module_data, dict):
            # Process each API in the module
            for api_name, api_data in module_data.items():
                if isinstance(api_data, dict):
                    # Add Docstring field
                    api_data['Docstring'] = create_docstring(api_data)
    
    return data


def main():
    """Main function to process all module JSON files and create API_data.json."""
    modules_dir = Path("data/modules")
    all_modules_data = {}
    
    # Iterate through each module directory
    for module_dir in modules_dir.iterdir():
        if module_dir.is_dir():
            module_name = module_dir.name
            
            # Look for JSON files in the module directory
            json_files = list(module_dir.glob("*.json"))
            
            for json_file in json_files:
                print(f"Processing {json_file}...")
                try:
                    module_data = process_module_json(json_file)
                    
                    # Merge the module data into all_modules_data
                    for key, value in module_data.items():
                        if key in all_modules_data:
                            # If key exists, merge the APIs
                            if isinstance(all_modules_data[key], dict) and isinstance(value, dict):
                                all_modules_data[key].update(value)
                        else:
                            all_modules_data[key] = value
                            
                except Exception as e:
                    print(f"Error processing {json_file}: {e}")
    
    # Sort modules alphabetically
    sorted_modules_data = dict(sorted(all_modules_data.items()))
    
    # Save the combined data to API_data.json
    output_path = Path("API_data.json")
    with open(output_path, 'w') as f:
        json.dump(sorted_modules_data, f, indent=2)
    
    print(f"\nAPI_data.json has been created with data from {len(sorted_modules_data)} modules.")
    print(f"Total APIs processed: {sum(len(v) for v in sorted_modules_data.values() if isinstance(v, dict))}")


if __name__ == "__main__":
    main()

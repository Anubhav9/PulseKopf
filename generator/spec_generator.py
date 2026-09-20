from models import metrics_model
import yaml

def return_spec_yaml():
    schema=metrics_model.MetricsModel.model_json_schema()
    yaml_schema = yaml.safe_dump(
        schema,
        sort_keys=False
    )
    return yaml_schema

def return_spec_status_yaml():
    schema=metrics_model.MetricsModelStatus.model_json_schema()
    yaml_schema = yaml.safe_dump(
        schema,
        sort_keys=False
    )
    return yaml_schema

def return_complete_crd():
    spec_yaml=return_spec_yaml()
    file_path = "resources/health_metrics_crd.yaml"

    with open(file_path, "r") as file:
        crd = yaml.safe_load(file)


    crd["spec"]["versions"][0]["schema"] = {
        "openAPIV3Schema": {
            "type": "object",
            "properties": {
                "spec": spec_yaml
            }
        }
    }
    crd["spec"]["versions"][0]["schema"]["openAPIV3Schema"]["properties"]["spec"] = yaml.safe_load(spec_yaml)

    with open(file_path, "w") as file:
        yaml.safe_dump(crd, file, sort_keys=False)


import fastapi
import uvicorn
import json
from os import environ
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi_cache.decorator import cache
from templates import generate_templates


config = json.load(open("config.json"))
templates = json.load(open("templates.json"))
app = fastapi.FastAPI()
FastAPICache.init(InMemoryBackend())


@app.get("/")
@cache(expire=1800)
def custom(
    templates_repo: str = config["Templates_Repo"],
    icon_path: str = config["Icon_Path"],
    server_icon: str = config["Server_Icon"],
    username: str = config["Username"],
    whitelist: str = config["Whitelist"],
    operators: str = config["Operators"],
    node_hostname: str = config["Node_Hostname"],
    latest_version: str = config["Latest_Version"],
    server_adress: str = config["Server_Adress"],
    custom: str = False,
):
    if custom:
        return json.loads(
            generate_templates(
                {
                    "Templates_Repo": templates_repo,
                    "Icon_Path": icon_path,
                    "Server_Icon": server_icon,
                    "Username": username,
                    "Whitelist": whitelist,
                    "Operators": operators,
                    "Node_Hostname": node_hostname,
                    "Latest_Version": latest_version,
                    "Server_Adress": server_adress,
                }
            )
        )
    return templates


if __name__ == "__main__":
    uvicorn.run(
        "server:app", host="0.0.0.0", port=8080, reload=environ.get("DEV", False)
    )

import pynecone as pc

config = pc.Config(
    telemetry_enabled=False,
    app_name="app",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    port=3000,
    #deploy_url="localhost",

    #bun_path="~/.bun/bin/bun"
    #bun_path="/app/.bun"
    bun_path="/usr/local/bin/bun",  # un-comment if you want to run in Docker
)

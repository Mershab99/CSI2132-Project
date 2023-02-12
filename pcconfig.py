import pynecone as pc

config = pc.Config(
    app_name="app",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    port="3000",
    # bun_path="/usr/local/bin/bun",  # un-comment if you want to run in Docker
)

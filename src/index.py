from js import Response
import json

async def on_fetch(request, env):
    teste = [1,2,3,4]
    a = []
    for e in teste:
        a.append(f"{e}--xxx")

    return Response.new(f" sucesso! {a} {env.name} ")

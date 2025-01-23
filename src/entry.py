from js import Response

async def on_fetch(request, env):
    return Response.new(f" {env.MY_VARIABLE} {env.OTHER_VARIABLE or None} sucesso! ")

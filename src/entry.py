from js import Response

async def on_fetch(request, env):
    return Response.new(f" sucesso! ")

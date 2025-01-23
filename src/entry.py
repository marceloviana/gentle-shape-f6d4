from js import Response

async def on_fetch(request, env):
    return Response.new(f"Hello World - Marcelo Viana teste! {env.MY_VARIABLE} {env.OTHER_VARIABLE or None}")

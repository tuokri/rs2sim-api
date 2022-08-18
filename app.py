import sanic
from sanic import HTTPResponse
from sanic import Request

app = sanic.Sanic(name="rs2sim-api")


@app.get("/")
async def root(_) -> HTTPResponse:
    return sanic.text("")


@app.post("/simulate")
async def simulate(request: Request) -> HTTPResponse:
    return sanic.json({})


if __name__ == "__main__":
    app.run(port=80)

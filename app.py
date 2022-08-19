import orjson
import sanic
import zstd
from rs2simlib.fast import sim as fastsim
from sanic import HTTPResponse
from sanic import Request

app = sanic.Sanic(name="rs2sim-api")


def dumps_gzip(data: dict) -> str:
    return zstd.dumps(orjson.dumps(
        data,
        option=orjson.OPT_SERIALIZE_NUMPY,
    ))


@app.exception(Exception)
async def on_error(request: Request,
                   exception: Exception) -> HTTPResponse:
    print(f"error on request: {request}: {exception}")

    return sanic.json({
        "message": "bad request",
    }, status=400,
    )


@app.get("/")
async def root(_) -> HTTPResponse:
    return sanic.text("")


@app.post("/simulate")
async def simulate(request: Request) -> HTTPResponse:
    sim_params = request.json
    sim_x, sim_y = fastsim.simulate(
        sim_time=5.0,
        time_step=1 / 500,
        drag_func=7,
        ballistic_coeff=0.25,
        aim_dir_x=1.0,
        aim_dir_y=0.0,
    )
    return sanic.json(
        body={
            "x": sim_x,
            "y": sim_y,
        },
        headers={
            "Content-Encoding": "zstd",
        },
        dumps=dumps_gzip,
    )


if __name__ == "__main__":
    app.run(
        auto_reload=True,
        debug=True,
    )

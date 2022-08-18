import sanic
from sanic import HTTPResponse
from sanic import Request

import sim

app = sanic.Sanic(name="rs2sim-api")


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
    sim_x, sim_y = sim.simulate(
        sim_time=5.0,
        time_step=1 / 500,
        aim_dir_x=1.0,
        aim_dir_y=0.0,
    )
    return sanic.json({
        "x": list(sim_x),
        "y": list(sim_y),
    })


if __name__ == "__main__":
    app.run(debug=True)

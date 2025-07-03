from fastapi import FastAPI, Header, HTTPException
import httpx

app = FastAPI()

BACKEND_HOST = "http://product-api.internal.example.com"

@app.get("/products")
async def get_products(x_env_target: str = Header(...)):
    headers = {
        "x-env-target": x_env_target
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BACKEND_HOST}/products", headers=headers)
        response.raise_for_status()
        return response.json()
    except httpx.RequestError as exc:
        raise HTTPException(status_code=502, detail=f"Error contacting backend: {exc}")
    except httpx.HTTPStatusError as exc:
        raise HTTPException(status_code=exc.response.status_code, detail=exc.response.text)

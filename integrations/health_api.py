import os

import httpx
import asyncio

API_KEY=os.getenv("HEALTH_API_KEY")

async def get_health_data(param_name,start_time,end_time):
    params={
        "type":param_name,
        "start_date":start_time,
        "end_date":end_time
    }
    headers={
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"BEARER {API_KEY}"
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://api.example.com/health",params=params,headers=headers)
            status_code=response.status_code
            if status_code == 200:
                return response.json()
            else:
                return {"error": f"Failed to fetch health data, status code: {status_code}"}
    except Exception as e:
        return {"error": str(e)}

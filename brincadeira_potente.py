import asyncio
import aiohttp

url = "site_aqui"

async def fazer_requisicao(session):
    async with session.get(url) as resposta:
        print(f"Código de status: {resposta.status}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fazer_requisicao(session) for _ in range(num_requisicoes)]
        await asyncio.gather(*tasks)

num_requisicoes = 100000
asyncio.run(main())

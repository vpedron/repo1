import uvicorn
 
if __name__ == "__main__":
 uvicorn.run("server.app:app", host="https://codrapinoticias.azurewebsites.net", port=5000, reload=True)

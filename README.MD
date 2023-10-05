This is a simple HTMX example/demo.
It uses Python FastAPI in the backend and HTMX in the frontend.

The Python server serves HTML content and the HTMX library is used to update the page content without reloading the page.

I built this to play around with HTMX and see that it works the way I need for a different project. 

## How to run

1. Clone the repo
2. install the requirements
`pip install fastapi uvicorn jinja2`
3. run the server
`uvicorn main:app --reload`
4. open the browser at http://localhost:8000

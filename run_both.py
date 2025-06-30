from multiprocessing import Process
import subprocess



def run_fastapi():
    from chatbot_main import run_api
    run_api()

def run_streamlit():
    # Launch via subprocess to invoke Streamlit properly
    subprocess.run(["streamlit", "run", "app.py"])

if __name__ == "__main__":
    p1 = Process(target=run_fastapi)
    p2 = Process(target=run_streamlit)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
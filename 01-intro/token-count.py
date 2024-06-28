import tiktoken

prompt = '''You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
    Use only the facts from the CONTEXT when answering the QUESTION.
    
    QUESTION: How do I execute a command in a running docker container?
    
    CONTEXT: 
    question: How do I debug a docker container?
answer: Launch the container image in interactive mode and overriding the entrypoint, so that it starts a bash command.
docker run -it --entrypoint bash <image>
If the container is already running, execute a command in the specific container:
docker ps (find the container-id)
docker exec -it <container-id> bash
(Marcos MJD)

question: How do I copy files from my local machine to docker container?
answer: You can copy files from your local machine into a Docker container using the docker cp command. Here's how to do it:
To copy a file or directory from your local machine into a running Docker container, you can use the `docker cp command`. The basic syntax is as follows:
docker cp /path/to/local/file_or_directory container_id:/path/in/container
Hrithik Kumar Advani

question: How do I copy files from a different folder into docker container’s working directory?
answer: You can copy files from your local machine into a Docker container using the docker cp command. Here's how to do it:
In the Dockerfile, you can provide the folder containing the files that you want to copy over. The basic syntax is as follows:
COPY ["src/predict.py", "models/xgb_model.bin", "./"]											Gopakumar Gopinathan'''

encoding = tiktoken.encoding_for_model("gpt-4o")

print(len(encoding.encode(prompt)))

# Choose your OS system
FROM python:3.13.0

# Log level
ENV PYTHONUNBUFFERED 1
ENV GOOGLE_API_KEY AIzaSyAGwFhf81sz2bfQT1XFQE0_KQrXryXQMy0

# Make working directory
RUN mkdir /polyteacher

# Change the current working directory
WORKDIR /polyteacher

# Copy and link
ADD . /polyteacher

# Install the libraries
RUN pip install -r requirements.txt
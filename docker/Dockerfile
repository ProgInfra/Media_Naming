FROM python:3.10-slim-bullseye as build
WORKDIR /usr/src/app
SHELL [ "/bin/bash", "-c" ]

RUN mkdir /.cache && chmod 777 -R /.cache

# Install PDM Globally
RUN pip install pdm

# Copy PDM files
COPY ./pyproject.toml .
COPY ./pdm.lock .
COPY ./README.md .

# Install Dependencies for production
RUN pdm install --production

# Copy Source files
COPY ./src .

# Build the project
RUN pdm build


FROM python:3.10-slim-bullseye
WORKDIR /usr/src/app
SHELL [ "/bin/bash", "-c" ]

# Get Built package
COPY --from=build /usr/src/app/dist/naming*.whl .

# Install package
RUN pip install ./naming-*.whl

# Add Alias to call the CLI
RUN echo -e '#!/bin/bash\npython -m naming $@' > /usr/bin/naming && chmod +x /usr/bin/naming

CMD [ "naming", "--help" ]

## AIOps Architecture Diagram

                            +---------------------+
                            |    Slack Users      |
                            +---------------------+
                                     |
                                     v
                            +---------------------+
                            |     Slack App       |
                            | (Slack Bolt/SDK)    |
                            +---------------------+
                                     |
                                     v
                            +---------------------+
                            |  Slack Bot (app.py) |
                            +---------------------+
                                     |
                                     v
                            +---------------------+
                            |   Task Engine       |
                            | (engine.py)         |
                            +---------------------+
                            /        |        \
                           /         |         \
                          v          v          v
              +----------------+ +----------------+ +----------------+
              |   Jira Client   | |  GitHub Client | | Terraform      |
              |   (jira.py)     | | (github.py)    | | Manager        |
              +----------------+ +----------------+ | (terraform.py) |
                                             \      +----------------+
                                              \
                                               v
                            +---------------------+
                            |   OpenAI Client     |
                            | (openai_integration.py) |
                            +---------------------+
                                     |
                                     v
                            +---------------------+
                            |   Docker Container  |
                            |  (Dockerfile)       |
                            +---------------------+
                                     |
                                     v
                            +---------------------+
                            |     Docker Compose  |
                            |  (docker-compose.yaml) |
                            +---------------------+
                                     |
                                     v
                            +---------------------+
                            |      Kubernetes      |
                            |      (Helm Chart)    |
                            +---------------------+
                                     |
                                     v
                            +---------------------+
                            |     IBM Cloud /     |
                            |       AWS Cloud      |
                            +---------------------+

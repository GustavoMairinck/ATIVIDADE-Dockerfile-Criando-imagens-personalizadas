# Calculadora Python com Docker

## Descrição

Nesta atividade, você deverá criar uma imagem Docker personalizada para uma aplicação simples em Python ou Node.js. O objetivo é aplicar os principais conceitos de construção de imagens, organização do contexto de build e boas práticas de desenvolvimento com Docker.

## Build da imagem

```bash
docker build -t calculadora-python:1.0 .
```

<img width="1116" height="674" alt="Captura de tela 2026-06-12 183952" src="https://github.com/user-attachments/assets/2f1e9dd5-78da-4464-93a2-5f0fe4a6a322" />

## Imagem criada

```bash
docker image ls
```

<img width="1912" height="144" alt="Captura de tela 2026-06-12 184044" src="https://github.com/user-attachments/assets/99ee0913-60ed-4117-b30f-6e7546faf14e" />

## Execução da calculadora

```bash
docker run -it --name calculadora calculadora-python:1.0
```

<img width="1185" height="277" alt="Captura de tela 2026-06-12 184207" src="https://github.com/user-attachments/assets/f4629cd6-a8bb-4220-ba24-b1fb2e6f4edc" />

## Estado do contêiner

```bash
docker ps -a
```

<img width="1325" height="99" alt="Captura de tela 2026-06-12 184233" src="https://github.com/user-attachments/assets/cb9e129e-4196-4d78-bae3-a3b5fa86a128" />

## Logs da aplicação

```bash
docker logs calculadora
```

<img width="1113" height="163" alt="Captura de tela 2026-06-12 190344" src="https://github.com/user-attachments/assets/745923ac-0ce1-4c00-afec-c8b5ed7efac9" />

## Remoção do contêiner

```bash
docker rm calculadora
```

<img width="876" height="101" alt="Captura de tela 2026-06-12 190529" src="https://github.com/user-attachments/assets/b4d1e980-7fba-404f-8e4b-6a29cf1a7fe1" />
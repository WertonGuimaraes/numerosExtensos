# Números em Extenso

Esse projeto consite em uma *API* que transfoma números inteiros em sua forma por extenso.

## Configuração
* Instale o [docker](https://tecadmin.net/install-docker-on-ubuntu/).
* Instale o [docker-compose](https://linuxize.com/post/how-to-install-and-use-docker-compose-on-ubuntu-18-04/).
* Dê poderes ao docker: 
```
sudo chown $USER /var/run/docker.sock
```

## Rodando o projeto

#### Inicializando
Após o pull do projeto entre na pasta *numerosExtensos* e execute o seguinte código:
```
docker-compose up -d --build
```
Isso fará que o projeto seja construido e as dependências baixadas, para que o projeto seja executado depois.

#### Parando
Para parar o servidor entre na pasta *numerosExtensos* e execute o seguinte código:
```
docker-compose down
```

## Consumindo a api

Get números inteiros por extenso.

Path: /{numero}

Method: GET

Exemplo: http://localhost:3000/**25**

Response Status

**200 - OK** 

É retornado um json onde mostrará o *{numero}* por extenso

Response Body:
```json
{"extenso":"vinte e cinco"}
```

**400 - OK** 

É retornado um json que mostrará um erro caso o *{numero}*:
- Não esteja no intervalo permitido.
- Não seja um numero inteiro.

Response Body:
```json
{"erro":"Só é aceitado números inteiros entre LIMITE_MINIMO e LIMITE_MAXIMO."}
```

```json
{"erro":"O valor recebido não é um inteiro."}
```




# ZKore Backend
A ZKML application to prove your off chain score on chain.

## Run
1. Run Backend
```shell
uvicorn server:app --reload
```

## API
1. api 
```shell
input : user_name (str)
get output : score (str)
```

2. api
```shell
input : selected rank (int) (from 1 to 5, low to high)
get output : {public_signal, proof} (dictionary)
```
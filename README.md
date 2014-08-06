# Reddit Snapchatter
On a very slow weekend I thought it would be a cool idea to write an app which sends me the top pics from reddit via Snapchat.

Uses the [PySnapchat Snapchat wrapper](https://github.com/itsnauman/PySnapchat) by @itsnauman.

To get it going you'll have to install snapchat, requests and PIL. Luckily this can all be done pretty easy using pip.

`pip install -r requirements.txt`

Then once you've mucked around getting PIL you'll need the password for the account which will be located in config.py. You'll need to decrypt this using `make decrypt_conf` and then entering the password.

`python main.py`

## License
It seems like all the cool cats have this section in their READMEs at the moment so I thought I'd hop on the band wagon. I don't know anything about licences though so just do what ever you want with this code as long as its not starting any wars or stuff

## Chur
Thanks for checking this out. Any pull requests would be mean as. Hit me up on twitter [@davecarpie](https://twitter.com/davecarpie)

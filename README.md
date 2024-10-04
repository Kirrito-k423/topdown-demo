# topdown demo for person

## debug

```bash
cd topdown-demo

# clone the hugo-theme-topdown 
git clone https://github.com/Kirrito-k423/hugo-theme-topdown.git themes/topdown

# deploy2local vitual box
hugo server --buildFuture -t topdown --bind=192.168.0.102 --baseURL=http://192.168.0.102 -p 1315 -D -d ./public

# deploy2local server
hugo server --buildFuture -t topdown --bind=222.195.72.221 --baseURL=http://222.195.72.221 -p 1315 -D -d ./public

# deploy2snode6
hugo server --buildFuture --themesDir /staff/shaojiemike/github/acsa-web-test/themes -t topdown --bind=222.195.72.221 --baseURL=http://222.195.72.221 -p 1315 -D -d ./public

# deploy2snode6 
hugo server --buildFuture --themesDir /staff/shaojiemike/github/acsa-web-test/themes -t topdown --bind=snode6.acsalab.com --baseURL=http://snode6.acsalab.com -p 1315 -D -d ./public
```

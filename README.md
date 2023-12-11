# topdown demo for person

## debug

```bash
# clone the hugo-theme-topdown 
git clone https://github.com/Kirrito-k423/hugo-theme-topdown.git themes/topdown
# deploy2local
hugo server --buildFuture -t topdown --bind=222.195.72.221 --baseURL=http://222.195.72.221 -p 1315 -D -d ./public

# for me to develop
 hugo server --buildFuture --themesDir /staff/shaojiemike/github/acsa-web-test/themes -t topdown --bind=222.195.72.221 --baseURL=http://222.195.72.221 -p 1315 -D -d ./public
```
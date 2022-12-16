mkdir -p /scratch/$USER/src
cd /scratch/$USER/src
rm -rf .git
git init
git remote add -f origin https://github.com/hwang2006/KISTI-DL-tutorial-using-horovod.git
git config core.sparseCheckout true
echo 'src/*' >>.git/info/sparse-checkout
git pull origin main
mv src/* .
rm -rf src

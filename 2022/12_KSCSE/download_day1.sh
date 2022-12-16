mkdir -p /scratch/$USER/workspace
cd /scratch/$USER/workspace
rm -rf .git
git init
git remote add -f origin https://github.com/yhgon/bootcamp_kr.git
git config core.sparseCheckout true
echo '2022/12_KSCSE/*' >>.git/info/sparse-checkout
git pull origin main
mv 2022/12_KSCSE/* .
rm -rf 2022

echo $0
echo $1
CONTAINS_MIGRATION=$1
echo $CONTAINS_MIGRATION
sudo docker-compose build server
sudo docker-compose down && docker-compose up -d
if $CONTAINS_MIGRATION
then 
    docker-compose run --rm --entrypoint "python3 manage.py migrate" server
fi
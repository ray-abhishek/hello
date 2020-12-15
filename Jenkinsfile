node {

    def env_vars = [
   'IN_DOCKER_CONTAINER=true',
   'IN_CI_ENV=true',
   'CI_DB_NAME=tests',
   'CI_DB_USER=root',
   'CI_DB_PASS=password',
   'CI_DB_HOST=mysql',
   'CI_DB_PORT=3306'
  ]

  def source_dir = "${env.WORKSPACE}@script"
  def rabbitmq_image = 'rabbitmq:3-management'
  def rabbitmq_args = '-e RABBITMQ_ERLANG_COOKIE="COOKIE" -e RABBITMQ_DEFAULT_USER="urbanpiper" -e RABBITMQ_DEFAULT_PASS="urbanpiper" -e RABBITMQ_DEFAULT_VHOST="uphost"'
  def mysql_image = 'dnhsoft/mysql-utf8:5.6'
  def mysql_args = '-e MYSQL_ROOT_PASSWORD="password" -v jenkins_mysql_db:/var/lib/mysql'
  def contains_migration = env.CONTAINS_MIGRATIONS ? env.CONTAINS_MIGRATIONS : ""

  stage('Build Image') {
    dir(source_dir) {
      sh 'docker build . -t server/image'
    }
  }
    try {
        stage('Run Tests') {
          dir(source_dir) {
            docker.image(rabbitmq_image).withRun(rabbitmq_args) { rc ->
            docker.image(mysql_image).withRun(mysql_args) { mc ->
              withEnv(env_vars) {
                docker.image('server/image').inside("--link=${mc.id}:mysql --link=${rc.id}:rabbitmq") {
                  sh 'find . -name *.pyc | xargs rm -f'
                  sh 'pytest -s -v'
                }
              }
            }
            }
          }
        }
        stage('Deploy') {
            dir(source_dir) {
              sh 'bash deploy_commands.sh ' + contains_migration
            }
        }
    }
    catch (err) {
        throw err
    }
}
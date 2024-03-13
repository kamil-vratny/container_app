# container_app

## enabling ECS Service for CodeDeploy
aws ecs update-service --service my-service --cluster my-cluster --deployment-configuration "deploymentCircuitBreaker={enable=true,rollback=true}" --deployment-controller type=CODE_DEPLOY

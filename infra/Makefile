AWS_PROFILE := gdslib
AWS_ID := $(shell python id.py ${AWS_PROFILE} account)
AWS_REGION := $(shell python id.py ${AWS_PROFILE} region)
COGNITO_DOMAIN := $(shell grep COGNITO_DOMAIN ../.env | sed s/COGNITO_DOMAIN=//g)
COGNITO_POOL_ID := $(shell grep COGNITO_POOL_ID ../.env | sed s/COGNITO_POOL_ID=//g)
COGNITO_CLIENT_ID := $(shell grep COGNITO_CLIENT_ID ../.env | sed s/COGNITO_CLIENT_ID=//g)
COGNITO_CLIENT_SECRET := $(shell grep COGNITO_CLIENT_SECRET ../.env | sed s/COGNITO_CLIENT_SECRET=//g)

vars:
	@echo AWS_ID=${AWS_ID}
	@echo AWS_PROFILE=${AWS_PROFILE}
	@echo AWS_REGION=${AWS_REGION}
	@echo COGNITO_DOMAIN=${COGNITO_DOMAIN}
	@echo COGNITO_POOL_ID=${COGNITO_POOL_ID}
	@echo COGNITO_CLIENT_ID=${COGNITO_CLIENT_ID}
	@echo COGNITO_CLIENT_SECRET=${COGNITO_CLIENT_SECRET}

apply:
	terraform apply -auto-approve

init:
	terraform init

login:
	${BROWSER} "https://${COGNITO_DOMAIN}.auth.${AWS_REGION}.amazoncognito.com/login?client_id=${COGNITO_CLIENT_ID}&response_type=code&scope=aws.cognito.signin.user.admin+email+openid&redirect_uri=https://gdslib.ai"

signup:
	${BROWSER} "https://${COGNITO_DOMAIN}.auth.${AWS_REGION}.amazoncognito.com/signup?client_id=${COGNITO_CLIENT_ID}&response_type=code&scope=aws.cognito.signin.user.admin+email+openid&redirect_uri=https://gdslib.ai"

logout:
	${BROWSER} "https://${COGNITO_DOMAIN}.auth.${AWS_REGION}.amazoncognito.com/logout?client_id=${COGNITO_CLIENT_ID}&response_type=code&scope=aws.cognito.signin.user.admin+email+openid&redirect_uri=https://gdslib.ai"

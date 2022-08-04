erDiagram
LogEntry{
AutoField id
DateTimeField action_time
TextField object_id
CharField object_repr
PositiveSmallIntegerField action_flag
TextField change_message
}
Permission{
AutoField id
CharField name
CharField codename
}
Group{
AutoField id
CharField name
}
ContentType{
AutoField id
CharField app_label
CharField model
}
Session{
CharField session_key
TextField session_data
DateTimeField expire_date
}
EmailAddress{
AutoField id
CharField email
BooleanField verified
BooleanField primary
}
EmailConfirmation{
AutoField id
DateTimeField created
DateTimeField sent
CharField key
}
SocialApp{
AutoField id
CharField provider
CharField name
CharField client_id
CharField secret
CharField key
}
SocialAccount{
AutoField id
CharField provider
CharField uid
DateTimeField last_login
DateTimeField date_joined
TextField extra_data
}
SocialToken{
AutoField id
TextField token
TextField token_secret
DateTimeField expires_at
}
TimeStampedModel{
BigAutoField id
DateTimeField created
DateTimeField updated
}
User{
BigAutoField id
CharField password
DateTimeField last_login
BooleanField is_superuser
CharField username
CharField email
BooleanField is_staff
BooleanField is_active
DateTimeField date_joined
CharField name
}
Tags{
BigAutoField id
DateTimeField created
DateTimeField updated
}
Series{
BigAutoField id
DateTimeField created
DateTimeField updated
}
Article{
BigAutoField id
DateTimeField created
DateTimeField updated
CharField title
CharField description
TextField content
CharField status
}
Blog{
BigAutoField id
CharField name
TextField description
}
LogEntry||--|{User : user
LogEntry||--|{ContentType : content_type
Permission||--|{Group : group
Permission||--|{User : user
Permission||--|{ContentType : content_type
Group||--|{User : user
Group||--|{Permission : permissions
ContentType||--|{LogEntry : logentry
ContentType||--|{Permission : permission
EmailAddress||--|{EmailConfirmation : emailconfirmation
EmailAddress||--|{User : user
EmailConfirmation||--|{EmailAddress : email_address
SocialApp||--|{SocialToken : socialtoken
SocialAccount||--|{SocialToken : socialtoken
SocialAccount||--|{User : user
SocialToken||--|{SocialApp : app
SocialToken||--|{SocialAccount : account
TimeStampedModel||--|{Tags : tags
TimeStampedModel||--|{Series : series
TimeStampedModel||--|{Article : article
User||--|{LogEntry : logentry
User||--|{EmailAddress : emailaddress
User||--|{SocialAccount : socialaccount
User||--|{Article : author
User||--|{Blog : authors
User||--|{Group : groups
User||--|{Permission : user_permissions
Tags||--|{TimeStampedModel : timestampedmodel_ptr
Series||--|{TimeStampedModel : timestampedmodel_ptr
Article||--|{TimeStampedModel : timestampedmodel_ptr
Article||--|{Blog : blog
Article||--|{User : author
Blog||--|{Article : article
Blog||--|{User : authors

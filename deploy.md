# Launch protocol for serverless app
Serverless applications can be launched as independent microservices which
Further instructions on creating a custom domain on AWS API Gateway can be found [here](https://medium.com/@maciejtreder/custom-domain-in-aws-api-gateway-a2b7feaf9c74)

1.
2.
3. Using a custom domain name

##

## 3. Using a custom domain name
### 3.1 Issue a certificate
In order to use Amazon services without traffic being rejected, an SSL certificate must be issued through Amazon's [Certificate Manager](https://www.aws.amazon.com) service.

 - Navigate to AWS Certificate Manager in the console
 - Certificates must be issued in US-east 1 (North Virginia) region, so make sure that your region is set to US-east 1 even if you are deploying your app in another region.
 - Choose `Request Public Certificate`
 - Choose domain names for which you would like to request a certificate. www.engmatthew.com and engmatthew.com will be treated as two separate domains, so a separate certificate will need to be requested for each.
  - INSERT IMAGE EXAMPLE
  - Select validation method. For DNS validation:
  - Amazon will provide a host and target. Copy these and create a new CNAME in your DNS service provider as directed. Your DNS service provider may add the domain to the host automatically. If this is the case you may need to remove the ending domain (eg, "ahds5mh6.engmatthew.com" would just be "ahds5mh6"). It can take several to 40 minutes for the CNAME to propagate.
  - INSERT IMAGE EXAMPLE
  - In Certificate Manager, complete the request for an SSL certificate by hitting `Confirm and request`
  - It will usually take several minutes to an hour to have your request approved. After 72 hours, if a request has not be approved, the request will automatically be cancelled. Ensure that your CNAME was created correctly.

### 3.2 Set up custom domain
 - Choose `Custom domain name` in API Gateway
 - Add a new custom domain name for each domain that you have
 - Take target domain name and create a new CNAME 

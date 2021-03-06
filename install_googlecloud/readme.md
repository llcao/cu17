# Get Started with `cloud.cs.columbia` account

Yizhou Wang

## Get a `cloud.cs.columbia.edu` account

Sign up for a `cloud.cs.columbia.edu` account at [Google Cloud - CS Columbia](https://www.cs.columbia.edu/auth/cloud). Note that is is an entirely new account and is not your normal Columbia account. 

Your cloud Columbia CS account will be in the form: `yourUNI@cloud.cs.columbia.edu`. 

After signing up, you will receive an email including your account ID and temporary password. 

Log in to your Google Cloud Platform(GCP) account [HERE](https://console.cloud.google.com/) using a **private browsing window** (this is useful to prevent you from redeeming the coupon to a wrong account). Change your password. 

You will get to this page if success. 

![GCP Start](https://github.com/llcao/cu17/blob/master/install_googlecloud/img/gcp_start.png)

## Redeem a coupon code

**Double Check** that you are logged in with `yourUNI@cloud.cs.columbia.edu` account!

Go to https://console.cloud.google.com/education. 

Enter the coupon code you have, and select *No* unless you actually want email updates on new offerings. Click on Accept and continue.

Then, GCP will create a project for you automatically.

To check your coupon is redeemed successfully, check the menu at upper left corner -> Billing. You can see your coupon there.

![coupon](https://github.com/llcao/cu17/blob/master/install_googlecloud/img/coupon.png)

## Create your project

Click the dropdown menu of projects, and click *Create project*. Enter your own project name and click *Create*.

![new project](https://github.com/llcao/cu17/blob/master/install_googlecloud/img/new_project_1.png)

## Generate a private/public key-pair (optional)

GCP provides a tutotrial for this step [HERE](https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys#createsshkeys).

I give you some sample commands for Mac/Linux:

``ssh-keygen -t rsa -f ~/.ssh/my_e6894_key -C [MY_UNI]``

``chmod 400 ~/.ssh/my_e6894_key``

For convenience, add the private key to your ssh-agent:

``ssh-add ~/.ssh/my_e6894_key``

**Add your public key to your GCP project:**

Go back to GCP -> Menu -> Compute Engine -> Metadata -> SSH Keys -> Add SSH keys.

View the content of `my_e6894_key.pub` by using command `vim ~/.ssh/my_e6894_key.pub`. Copy the content start with `ssh-rsa` to GCP. 

Click *Save*.

## Create virtual machine instance

Use [calculators](https://cloud.google.com/pricing/calculators) provided by Google cloud to get a preview of pricing and choose a suitable machine for you.

Look at [this tutorial](https://cloud.google.com/compute/docs/gpus/add-gpus), or [this README](https://github.com/llcao/cu17/blob/master/install_googlecloud/install_gcloud.md).

## Resize your persistent disk

I think you need to resize the persistent disk for your instance because it's usually too small. Please have a look at [this tutorial](https://cloud.google.com/compute/docs/disks/add-persistent-disk).

## Accessing VM instance

You can use **Google Cloud Shell** to access your instance easily.

![gshell](https://github.com/llcao/cu17/blob/master/install_googlecloud/img/gshell.png)

You can also use **SSH** to access your instance.

`ssh [user_name]@[external_IP_address]`

Sample command:

`ssh [myUNI]@104.196.107.142`

## Notations

Remember to [stop/terminate your instance](https://cloud.google.com/compute/docs/instances/stopping-or-deleting-an-instance) when you are not using it. "A stopped instance does not incur charges, but all of the resources that are attached to the instance will still be charged." 

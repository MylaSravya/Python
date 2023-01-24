## 1) What is AWS S3?
Amazon S3 (Simple Storage Service) provides an object storage, which is designed for storing and recovering an arbitrary amount of information or data from anywhere over the internet. This storage is provided through a web services interface. It offers 99.999999999% durability and 99.99% availability of objects. It can also store computer files up to 5 terabytes in size.

## 2) What are the benefits of AWS Simple Storage Service?
* **Durability:** It gives 99.999999999 percent SLA.
* **Cheaper:** It supports a variety of storage classes. They range from those files that need to be accessed more frequently, like caching, to files that rarely change, like snapshots.
* **Scalability:** Storage resources can be easily scaled up or down based on your organization’s needs.
* **Availability:** The availability of objects on S3 is 99.99 percent
* **Security:** It offers a robust suite of tools for access management and encryption that provide enhanced security.
* **Flexibility:** The Simple Storage Service is perfect for a wide range of uses, including data storage, backups, software delivery, archiving, disaster recovery, hosting websites, mobile applications, IoT devices, and much more.
  
## 3) What is the use of AWS S3?
S3 is Amazon’s object storage service. Using Amazon Simple Storage Service, we can store and retrieve any amount of data from anywhere on the internet at any time.

## 4) What is an Object in AWS S3?
The Amazon S3 object store lets you store any number of objects using unique keys. The objects can be stored in one or more buckets, and each bucket can hold up to 5 TB of data.

## 5) What is Key in AWS S3?
Keys are unique identifiers of objects within a bucket. Each bucket has exactly one key. An object is uniquely identified by its bucket, object key, and optionally, version ID (if Simple Storage Service Versioning is enabled for the bucket). As a result, you can think of Amazon Simple Storage Service as a basic mapping between “bucket + key + version” and the actual object.

## 6) Explain S3 Versioning.
The Amazon S3 Versioning feature allows you to keep multiple variants of the same object in the same bucket. Objects stored in S3 buckets can be preserved, retrieved, and restored with Simple Storage Service Versioning. It is easy to recover from both unintentional user actions and application failures.

## 7) What is Bucket Policy?
Bucket policies allow you to grant access permissions to objects within your bucket by using AWS IAM policies. A bucket policy can only be associated with the bucket owner. An owner of a bucket can assign permissions to any object in the bucket that is attached to the bucket.

## 8) What is Access control lists (ACLs) ?
The ACL allows you to grant read-only and write-only access to individual buckets and objects to authorized users. ACLs are attached to buckets and objects as sub-resources. ACLs are an older access control system for defining the which AWS accounts or groups are granted access and the type of access.

## 9) How large can a Simple Storage Service bucket be?
You can store an unlimited amount of data and objects in an Simple Storage Service bucket. The size of a single Amazon S3 object can range from 0 bytes to 5 terabytes. An object of around 5 GB can be uploaded in a single upload request but Multipart Upload must be enabled.

## 10) Explain the benefits of S3 versioning.
We can store multiple variants of an object in a bucket by versioning it. An object can be restored to a previous or specific version by versioning. If an object is deleted or accidentally overwritten, versioning can be used to recover it.

## 11) How to configure S3 Versioning on a Bucket?
Versioning helps you keep multiple versions of an object in one place. Follow these steps to enable versioning on an S3 bucket.

* Login to your AWS account.
* Choose Simple Storage Service service.
* Choose a bucket for which versioning should be enabled.
* Go to the properties tab.
* Select versioning from properties.
* Click on the OK button to enable versioning.

## 12) Is Simple Storage Service considered as DFS?
Simple Storage Service is not a distributed file system, but rather a binary object store. It is structured like a filesystem and is often used like one. Each bucket is a new database (meaning, folder), with keys as folder paths and values as binary objects (i.e. files).

## 13) How to create an S3 bucket?
To create an AWS S3 bucket check our solution blog for the same.

## 14) Can I Upload Files Using The AWS Console?
Yes, you can use either of two ways to upload files using AWS Console. One way is by clicking on Objects and selecting your bucket, then uploading a file to it. The other way is by navigating through a bucket’s properties. This is useful if you need to include objects that are not visible in your console, such as large audio or video files.

## 15) What is the command to list objects in Simple Storage Service bucket?
To list all files or objects under a specified directory or prefix, use the aws s3 ls –recursive command on the AWS CLI .

## 16) What are the Storage Classes available in Amazon S3?
* S3 Standard
* S3 Standard IA
* S3 one zone-infrequent access
* S3 Glacier

## 17) Which storage class does AWS S3 use by default?
Standard

## 18) What are the ways to manage access for Amazon S3 buckets?
* IAM helps manage Users, Groups, and Roles.
* ACL helps manage objects via access control lists.
* S3 Access Points Helps manage data sets using access points specific to each application.
* Bucket policies help in managing resources and permissions.

## 19) How do I delete an AWS S3 bucket?
For deleting an AWS Simple Storage Service  bucket, follow these steps:
* Log in to the Amazon Web Services Management Console.
* Select the Simple Storage Service.
* Locate the bucket you wish to delete.
* Press the delete button. AWS will ask you to type the bucket name you wish to delete.
* Enter the bucket name and click Confirm.

## 20) What is CloudFront in Amazon S3?
CloudFront is a content delivery web service. CloudFront provides fast, cost-effective delivery of websites, videos, APIs, images, and applications to users around the world.
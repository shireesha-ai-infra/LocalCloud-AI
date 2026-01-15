# Request Flow: From Browser to Application

This document explains what happens when a user accesses:

https://localcloud-ai.local

## Step 1: DNS Resolution
The browser resolves the domain name to an IP address.

## Step 2: TCP Connection
A reliable TCP connection is established to the server on port 443.

## Step 3: TLS Handshake
The browser verifies the server certificate and establishes an encrypted channel.

## Step 4: HTTP Request
An HTTP request is sent over the secure connection and processed by the application.

# Yeastar Central Management API: Python Wrapper
Python wrapper/SDK for the Yeastar Central Management API.

## Why?

My workplace has the need for some automation tools to do with the YCM, including for billing information and general monitoring of our clients systems. This started as a quick script that only pulled information about existing PBXs, but I've decided to try and implement the entire YCM API into easily usable Python functions.

Currently the wrapper is based on the Python `requests` module, but later on I may switch to `urllib3` to reduce external dependencies.

This wrapper is made following the documentation from Yeastar available [here](https://help.yeastar.com/en/yeastar-central-management/ycm-api/yeastar-central-management-developer-guide.html).

## To Do
- [ ] Create `createPbx` in `cloudpbx` functions
- [ ] Create `sendPbxActivationEmails` in `cloudpbx` functions
- [ ] Create `updatePbxDIDs` in `cloudpbx` functions
- [ ] Finish `createSharedRegisterTrunk` in `sharedtrunk` functions
- [ ] Finish `createPeerRegisterTrunk` in `sharedtrunk` functions
- [ ] Finish `sharedtrunk` function set
- [ ] Switch to `urllib3` from `requests`
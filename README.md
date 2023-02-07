![solidity1](Images/solidity1.png)
# **Columbia University Engineering, New York FinTech Bootcamp** 
# **August 2022 Cohort**
# **Capstone - building smart contracts to automate FinTech institutional financial processes and features.**


Objective - to automate the creation of joint savings accounts. 

Scenario - Fintech startup new hire, tasked with automating creation of joint savings accounts; will accept two addresses, which will possess account control.

Product - Solidity smart contract that accepts two user addresses. 
> Addresses will be able to control a joint savings account. 
> Use ether management functions to implement institutional requirements for provision of features. 
> Features will consist of the ability to deposit and withdraw funds from the account.

 
![Ether](Images/Ether.png)

### Product 


Initial compile & deploy
![compile&deploy](Execution_Results/compile_deploy.png)
Depositing one Ether as wei
![one_as_wei](Execution_Results/one_eth_as_wei.png)
Depositing ten Ether as wei
![ten_as_wei](Execution_Results/ten_eth_as_wei.png)
Depositing five Ether
![five_ether](Execution_Results/five_ether.png)
Set Account1 and Account2
![set_accounts](Execution_Results/set_accounts_one_two.png)
Withdrawing five ether to Account1
![five_for_one_A](Execution_Results/five_eth_account_one1.png)
![five_for_one_B](Execution_Results/five_eth_account_one2.png)
Withdrawing ten ether to Account2
![ten_for_two](Execution_Results/ten_eth_account_two.png)
___

## **Technologies**
___


### **Dependencies**

This challenge leverages Solidity with the following to compile and deploy the decentralized application (dapp):

* [Remix Ethereum IDE](https://remix-project.org/) - Remix IDE, is a no-setup tool with a GUI for developing smart contracts.
* [Ganache](https://trufflesuite.com/ganache/) - Quickly fire up a personal Ethereum blockchain which you can use to run tests, execute commands, and inspect state while controlling how the chain operates.
* [MetaMask](https://metamask.io/) - A crypto wallet & gateway to blockchain apps
* [streamlit] (https://) - 
___

### **Hardware used for development**

MacBook Pro (16-inch, 2021)

    Chip Appple M1 Max
    macOS Venture version 13.0.1

### **Development Software**

Homebrew 3.6.11

    Homebrew/homebrew-core (git revision 01c7234a8be; last commit 2022-11-15)
    Homebrew/homebrew-cask (git revision b177dd4992; last commit 2022-11-15)

Python Platform: macOS-13.0.1-arm64-arm-64bit

    Python version 3.9.15 packaged by conda-forge | (main, Nov 22 2022, 08:52:10)
    Scikit-Learn 1.1.3
    pandas 1.5.1
    Numpy 1.21.5

pip 22.3 from /opt/anaconda3/lib/python3.9/site-packages/pip (python 3.9)


git version 2.37.2

---
## *Installation of application (i.e. github clone)*

In the terminal, navigate to directory where you want to install this application from the repository and enter the following command

```python
git clone git@github.com:Billie-LS/Lucky_Bar_NFT_menu_of_surprise.git
```

---
## **Usage**

Using your web browser, to [REMIX_IDE](https://remix-project.org/) and initialize Remix Online IDE.  Then load the application from the project folder where you've installed the application:

```python
initiate the Solidity Compiler
```

In the Remix IDE, navigate to the “Deploy & Run Transactions” pane, and then make sure that “JavaScript VM” is selected as the environment
```python
Deploy & Run Transactions 
```

In the Remix IDE, Click the Deploy button to deploy the smart contract
```python
Deploy 
```
___

To use the smart contract, follow the key steps described as below:

- Clone the repository and load ***SOMETHING*** and ***SOMETHING.sol*** in Remix IDE. You may see the web console view as:

![Smart Contract](Images/App_Usage.png)

- While deploying, select Remix VM (London) as a sandbox environment.

- You may compile and deploy the smart contract to use it further.

- In order to integrate Remix IDE with MetaMask and MetaMask with Ganache, you may an article [here](https://www.geeksforgeeks.org/how-to-set-up-ganche-with-metamask/).

- Choose 'Injected Provider - MetaMask' as a sandbox blockchain Environment to connect Remix IDE with MetaMask. 

## **Version control**

Version control can be reviewed at:

```python
https://github.com/Billie-LS/Lucky_Bar_NFT_menu_of_surprise
```

[repository](https://github.com/Billie-LS/Lucky_Bar_NFT_menu_of_surprise)


___

### **Contributors**

Dinesh Mandal
    [LinkedIn](https://www.linkedin.com/in/dineshmandal/)
    [@GitHub](https://github.com/dinesh-m)

Loki 'billie' Skylizard
    [LinkedIn](https://www.linkedin.com/in/l-s-6a0316244)
    [@GitHub](https://github.com/Billie-LS)

Galiya Khusniyarova
    [LinkedIn](https://www.linkedin.com/in/galiya-khusniyarova-3470a6110/)
    [@GitHub](https://github.com/galiyaKhusniyarova)

Alexandra Paiz
    [LinkedIn](https://www.linkedin.com/in/alexandra-paiz-5b28b6241/)
    [@GitHub](https://github.com/alexandrapaiz)

Brock Denton
    [LinkedIn](https://www.linkedin.com/in/brock-denton-7850221a7/)
    [@GitHub](https://github.com/Brock-Denton)




### **BootCamp lead instructor**

Vinicio De Sola
    [LinkedIn](https://www.linkedin.com/in/vinicio-desola-jr86/)
    [@GitHub](https://github.com/penpen86)


### **BootCamp teaching assistant**

Santiago Pedemonte
    [LinkedIn](https://www.linkedin.com/in/s-pedemonte/)
    [@GitHub](https://github.com/Santiago-Pedemonte)

___

### **Additional references and or resources utilized**

[st.success](https://docs.streamlit.io/library/api-reference/status/st.success)

___
## **License**

MIT License

Copyright (c) [2022] [Dinesh Mandal, Loki 'billie' Skylizard, Galiya Khusniyarova, Alexandra Paiz, Brock Denton]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.




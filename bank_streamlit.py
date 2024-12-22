import streamlit as st
st.title("Welcome to ABC Bank")


class Bank:
    bal = 10000
    counter = 1

    def validate(self):
        tries = 1
        while tries <= 3:
            n = st.number_input("Enter pin number:", min_value=0)
            pin = 1234
            if st.button("Validate"):
                tries = tries+1
                if pin == n:
                    tries = 0
                    self.view()
                else:
                    if tries == 3:
                        st.warning("Too many chances")
                        exit()
                    else:
                        st.warning("Please enter a valid pin number")

    def view(self):
        while True:
            if st.button("Deposit"):
                self.deposit_amt()
            if st.button("Withdraw"):
                self.withdraw_amt()
            if st.button("Balance Enquiry"):
                self.balance_enquiry()
            if st.button("Exit"):
                exit()

    def deposit_amt(self):
        deposit = st.number_input("Enter amount to deposit")
        if deposit < 100:
            st.warning("Deposit amount should not be lesser than 100/- ")
        elif deposit > 50000:
            st.warning("Deposit amount should not be greater than 50000/- ")
        elif (deposit % 100) != 0:
            st.warning("Deposit amount should be multiple of 100")
        else:
            self.bal = self.bal + deposit
            st.success("Deposited successfully")

    def withdraw_amt(self):
        while True:
            if self.counter <= 3:
                withdraw = int(input("Enter amount to withdraw"))
                if withdraw < 100:
                    st.warning("Minimum withdrawal amount should be 100/-")
                elif (withdraw % 100) != 0:
                    st.warning("Withdraw amount should be multiple of 100")
                elif withdraw > self.bal:
                    st.warning("Insufficient funds")
                elif withdraw > (self.bal - 500):
                    st.warning("Minimum account balance should be maintained i.e; 500/-")
                elif withdraw > 20000:
                    st.warning("Maximum amount to be withdrawn is only 20000/-")
                else:
                    self.bal = self.bal - withdraw
                    self.counter = self.counter + 1
                    st.success("Withdraw successful")
                    self.view()
            else:
                print("Maximum transactions limit reached")
                self.view()

    def balance_enquiry(self):
        st.success("Your account balance is", self.bal, "/-")


obj = Bank()
obj.validate()

# Install Courier SDK: pip install trycourier
from trycourier import Courier

client = Courier(auth_token="pk_prod_QX1JJGYKD44W5NJ6YVBP5JKDY1GX")

resp = client.send_message(
  message={
    "to": {'zaeem.k.khan@gmail.com'
    },
    "template": "G1YK4YVZ68MT5WM5XBH4VGJWKNZ1",
    "data": {
      "variables": "awesomeness",
    },
  }
)

print(resp['zaeem.k.khan@gmail.com'])

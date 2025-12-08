# General Project Notes

* A multi-tiered architecture was not used for this project because some of the team members did not have enough experience in Docker to do it.
* The `init` file does not pass pycodestyle's checks. If the `init` file's imports are moved then there is a circular import issue and the project does not run. So, the `init` file is the only file in the project to not abide by PEP-8 standards.
* All of the other Python files in this project pass pycodestyle's checks.
* Instead of having plant listings be marked as "sold out", the team decided to allow plant listings to have a quantity of zero. That way, the plant seller can see which of their plants have sold out while their competitors and customers do not see the plant with a quantity of zero listed. This also allows the plant seller to restock the plant instead of having to delete the plant listing.
* If a customer leaves a plant in their cart and its stock becomes zero before they can check out, their cart will automatically remove the plant from it. Additionally, if the plant stock is less than the plant quantity added to the customer's cart, the cart item quantity will be updated to the current plant stock.
* The `.coverage` file generated for this project will be included in the `test_evidence` folder.
* To easily run the project in a Docker container, use the provided `deploy_container.sh` script.

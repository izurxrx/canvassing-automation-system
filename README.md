# Canvassing Automation System

## 1. Project Vision

To create a simple, efficient, and scalable system to automate the canvassing, quoting, and data management process for a procurement business. The system will consist of two main components:

1.  **A simple Mobile App** for canvassers in the field.
2.  **A powerful Web App** for the Admin to manage operations.

The primary goal is to minimize manual data entry, reduce the time it takes to generate quotes, and build a valuable, long-term database of product pricing information.

---

## 2. User Roles

### a. The Admin (You)

*   **Responsibilities:** Manages customer requests, creates canvassing lists, reviews incoming data, builds quotes, and maintains the product database.
*   **Platform:** Web App (desktop browser).

### b. The Canvasser (Your Team)

*   **Responsibilities:** Travels to stores to find products and prices.
*   **Platform:** Mobile App (iOS or Android).
*   **Key Constraint:** The app must be extremely simple and require minimal technical skill. The workflow should be as close to "point, shoot, and tap" as possible.

---

## 3. Core Features & Workflow

### a. The Admin Web App

The Admin dashboard is the central hub for all operations.

#### **Feature: Canvass List Management**
1.  **Create Canvass List:** The Admin receives a list of items from a customer (e.g., a school AO).
2.  **Enter Items:** The Admin creates a new "Canvass List" in the web app and types in the names of the items to be found (e.g., "A4 Paper," "Whiteboard Markers," "No. 2 Pencils").
3.  **Assign to Canvasser (Future Feature):** The Admin can assign the list to a specific canvasser.

#### **Feature: Live Canvassing Dashboard**
1.  **Real-time View:** The Admin has a dashboard that shows the active canvass lists.
2.  **Incoming Photos:** As canvassers upload photos, they appear automatically under the correct item.
3.  **OCR Price Suggestion:** The system uses Optical Character Recognition (OCR) to automatically read the price from each photo and suggests it.
4.  **Admin Review & Verification:** The Admin reviews the photo and the suggested price, corrects it if necessary, and adds any notes (e.g., store name, brand).

#### **Feature: Master Product Database**
1.  **Save to Database:** For any canvassed item, the Admin can click a **"Save to Master Products"** button. This saves the product's details (name, brand, store, verified price, and photo) into a permanent database.
2.  **Track Price History:** The system keeps a record of price changes for each product over time.
3.  **Auto-suggest from Database:** When creating a *new* canvass list, if an item (e.g., "A4 Paper") already exists in the Master Product Database, the system will instantly show the last known price. The Admin can then decide to:
    *   **Use the existing price** for the quote (if it's recent).
    *   **Request a new canvass** for that item to get fresh pricing.

#### **Feature: Quote Generation**
1.  **Select Products:** The Admin selects the best option for each item from the canvassed data or the Master Product Database.
2.  **Add Markup/Fee:** The system allows the Admin to add their service fee or markup.
3.  **Generate Quote:** The Admin clicks a button to generate a clean, professional quote (e.g., as a PDF) to send to the customer.

### b. The Canvasser Mobile App

The mobile app is designed for speed and simplicity.

#### **Feature: Simple Canvass List View**
1.  **View Assigned Lists:** The canvasser opens the app and sees the list of items they need to find for the day.
2.  **Simple To-Do Format:** The list is presented as a simple checklist.

#### **Feature: "Tap and Snap" Workflow**
1.  **Select Item:** The canvasser finds an item in a store (e.g., A4 paper). They tap "A4 Paper" on their list in the app.
2.  **Take Picture:** This action opens their phone's camera.
3.  **Snap Photo:** They take a clear picture of the product **and its price tag**.
4.  **Upload:** The photo is automatically uploaded and tagged to "A4 Paper".
5.  **No Typing Required:** The canvasser does not need to enter any text. Their only job is to correctly match the photo to the item on the list. The app handles the rest.
6.  **Add Multiple Options:** The canvasser can repeat this process for the same item at different stores or for different brands, adding multiple photo options for the Admin to review.

---

## 4. Technology Stack (Proposed)

*   **Backend (Web App Logic):** Python with a web framework like Django or Flask.
*   **Frontend (Web App UI):** A modern JavaScript framework like React or Vue.js for a responsive user experience.
*   **Mobile App:** A cross-platform framework like React Native or Flutter to build for both iOS and Android from a single codebase.
*   **Database:** PostgreSQL for robust data storage.
*   **OCR Engine:** Tesseract (via a Python library like `pytesseract`) for price extraction from images.
*   **Deployment:** GitHub for code hosting, with deployment to a cloud provider like Heroku, Vercel, or AWS.

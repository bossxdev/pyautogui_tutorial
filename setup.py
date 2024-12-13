from setuptools import setup, find_packages

setup(
    name="pyautogui_tutorial",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "opencv-python",
        "pyautogui",
        "numpy",
        "openpyxl",
    ],
    python_requires=">=3.6",
)

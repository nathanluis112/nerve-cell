from PIL import Image
import requests
import streamlit as st


#TITLE PAGE

st.set_page_config(page_title="My Webpage", page_icon="🧠",layout="wide")

#ASSETS
CellBody = Image.open("images/factory.png")
Nucleus = Image.open("images/manager.png")
Dendrites = Image.open("images/mailbox.png")
Axons = Image.open("images/mailman.png")
Mye = Image.open("images/marshmallow.png")
Syn = Image.open("images/hose.png")
Mito = Image.open("images/engine.png")
ER = Image.open("images/line.png")
Gol = Image.open("images/Package.png")
Rib = Image.open("images/engineer.png")
Lys = Image.open("images/waste.png")
Nod = Image.open("images/rest.png")

#HEADER#
with st.container():
    st.subheader("Group 1 12B")
    st.title("Nerve cells, also known as NUERONS")
    st.write("A wwebsite that provides information on the parts of a nerve cell")
    
#Cell Body (Soma)
    
with st.container():
    st.write("---")
    image_column, text_column = st.columns(2)
    with image_column:
        st.image(CellBody)
    with text_column:
        st.header("Cell Body (Soma)")
        st.write("##")
        st.write(
            """
            The cell body can be thought of as the factory itself.
            - Contains the nucleus
            - Maintains the health of the nueron          
            
            """
        )
        
        
#Nucleus
    
with st.container():
    st.write("---")
    text_column, image_column = st.columns(2)
    with image_column:
        st.image(Nucleus)
    with text_column:
        st.header("Nucleus")
        st.write("##")
        st.write(
            """
            The nucleus is like a factory manager who knows important information like its genetic material and instructions on how to build and maintain the cell as well as sending and receiving signals from around the cell.
            - Controls cells activities         
            
            """
        )
        
#Dendrites
    
with st.container():
    st.write("---")
    image_column, text_column = st.columns(2)
    with image_column:
        st.image(Dendrites)
    with text_column:
        st.header("Dendrites")
        st.write("##")
        st.write(
            """
            The dendrites are like a mailbox receiving info in the form of chemicals released by the axon terminals of other neurons. 
            - Receive signals from other neurons & transmit them to the cell body       
            
            """
        )
        
#Axons
    
with st.container():
    st.write("---")
    text_column, image_column = st.columns(2)
    with image_column:
        st.image(Axons)
    with text_column:
        st.header("Axon")
        st.write("##")
        st.write(
            """
            The axon terminals are like the senders of the mail which send chemical signals to the dendrites. 
            - Transmits electrical impulses from the cell body to other neurons or muscles       
            
            """
        )
        
#Myelin Sheath
    
with st.container():
    st.write("---")
    image_column, text_column = st.columns(2)
    with image_column:
        st.image(Mye)
    with text_column:
        st.header("Myelin Sheath")
        st.write("##")
        st.write(
            """
            Think of the myelin sheath as the plastic insulation that covers the wires of an electrical cord because it allows the electrical impulses to travel quickly and efficiently between one nerve cell and the next. 
            - A fatty layer that insulates the axon & helps speed up electrical impulses       
            
            """
        )
        
#Synaptic Terminals
    
with st.container():
    st.write("---")
    text_column, image_column = st.columns(2)
    with image_column:
        st.image(Syn)
    with text_column:
        st.header("Synaptic Terminals")
        st.write("##")
        st.write(
            """
            Synaptic terminals are like the nozzles at the end of a garden hose. Just as water flows through the hose and sprays out at the nozzle to nourish plants, electrical signals travel down the nerve cell and are released as chemical messengers at the synaptic terminals to add information to other cells 
            - Transfers the chemical signals from neuron to neuron    
            
            """
        )
        
#Mitochondria
    
with st.container():
    st.write("---")
    image_column, text_column = st.columns(2)
    with image_column:
        st.image(Mito)
    with text_column:
        st.header("Mitochondria")
        st.write("##")
        st.write(
            """
            The mitochondria is the engine of the nerve cell which is required to provide the car with energy to function.
            - Provides energy to the cell       
            
            """
        )
        
#Endoplasmic Reticulum (ER)
    
with st.container():
    st.write("---")
    text_column, image_column = st.columns(2)
    with image_column:
        st.image(ER)
    with text_column:
        st.header("Endoplasmic Reticulum (ER)")
        st.write("##")
        st.write(
            """
            The endoplasmic reticulum (ER) is like a factory's assembly line. In a factory, raw materials are processed and assembled into finished products.
            - The ER processes and folds proteins (in the rough ER) and assembles lipids (in the smooth ER), preparing them for use inside the cell or for transport to other locations 
             
            
            """
        )

#Ribosomes
    
with st.container():
    st.write("---")
    image_column, text_column = st.columns(2)
    with image_column:
        st.image(Rib)
    with text_column:
        st.header("Ribosomes")
        st.write("##")
        st.write(
            """
            Is the construction department responsible for building the proteins needed for various tasks within the city based on instructions from the mayor’s office. (Nucleus) 
            - The site of protein synthesis in the cell       
            
            """
        )
        
#Golgi Apparatus
    
with st.container():
    st.write("---")
    text_column, image_column = st.columns(2)
    with image_column:
        st.image(Gol)
    with text_column:
        st.header("Golgi Apparatus")
        st.write("##")
        st.write(
            """
            Responsible for packaging and shopping our proteins and materials within or outside the cell given the task of being the post office.  
            - Prepares, modifies, and sorts proteins from the endoplasmic reticulum      
            
            """
        )
        
#Lysosomes
    
with st.container():
    st.write("---")
    image_column, text_column = st.columns(2)
    with image_column:
        st.image(Lys)
    with text_column:
        st.header("Lysosomes")
        st.write("##")
        st.write(
            """
            The waste management department, which is responsible for cleaning up debris and recycling materials in order to keep the city tidy.  
            - Degradative and signaling functions       
            
            """
        )
        
#Nodes of Ranvier
    
with st.container():
    st.write("---")
    text_column, image_column = st.columns(2)
    with image_column:
        st.image(Nod)
    with text_column:
        st.header("Nodes of Ranvier")
        st.write("##")
        st.write(
            """
            The Nodes of Ranvier are like rest stops along a highway. Just as rest stops allow vehicles to refuel and continue their journey more efficiently, the Nodes of Ranvier help electrical signals "recharge" as they travel down the axon.
            - Allows for ions to diffuse in and out of the neuron, propagating the electrical signal down the axon       
            
            """
        )
        
# generate_docs.py
def generate_markdown_content():
    # Generate your Markdown content here
    # Claire Holmes August 2023
    # prints the NSD images and their HED annotations to a markdown file for a Read the Docs page 

    import pandas
    from mdutils.mdutils import MdUtils

    # load tsv of image identifiers and annotations
    shared1000 = pandas.read_table('././shared1000_HED.tsv')

    # start markdown file
    mdFile = MdUtils(file_name='nsd_images_annotations', title='Images and Annotations', author= 'Claire Holmes')

    # set up headers for table
    mdFile.new_line('The images on this webpage have been downsampled from [425, 425] to [200, 200] for upload to GitHub and this webpage.\n')
    mdFile.new_line('**Only the first 4 images have been uploaded to GitHub and displayed here as an example. All images will be uploaded pending input from collaborators. All links to COCO images should be working. (note: actual NSD images may be a cropped version of the COCO image. The cropped version is the one displayed here and on GitHub)**\n')
    mdFile.new_line('|Image|HED annotation|')
    mdFile.new_line('|---|---|\n')

    for i in range(1000):
        # get filename from tsv
        file_name = shared1000.File_Name[i]
        # filename changed to get downsampled images
        file_name = file_name[:-4] + '_downsampled.png'

        # write/print the image (from it's reference)
        mdFile.write('|![' + file_name[:10] + '][' + str(i+1) + ']')
        # path to get the image (from the filename)
        path = './downsampled1000/' + file_name
        # write the reference to the image file
        mdFile.new_reference_image(file_name, path, str(i+1))
    
        # get the coco ID from the tsv 
        cocoID = shared1000.cocoId[i]
        # caption the image with the link to the uploaded image on GitHub and the corresponding image on COCO
        mdFile.write('<br>[Image on GitHub](https://github.com/holmesclaire/nsd_hed_labels/blob/main/docs/downsampled1000/' + file_name + ')<br>[Image on COCO](https://cocodataset.org/#explore?id=' + str(cocoID) + ')')
        # write the annotation from the tsv
        annotation = shared1000.HED_short[i]
        mdFile.write('|' + annotation + '|\n')

    # create the markdown file
    return mdFile.create_md_file()

if __name__ == "__main__":
    markdown_content = generate_markdown_content()
    with open("generated_docs.md", "w") as f:
        f.write(markdown_content)

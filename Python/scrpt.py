import xlrd
import unidecode
hojaExcel = xlrd.open_workbook('/home/nexus/Code/Python/scriptExcel/lista wb 2019 ccompleta.xlsx').sheet_by_index(0)
encabezado = 'Handle,Title,Body (HTML),Vendor,Type,Tags,Published,Option1 Name,Option1 Value,Option2 Name,Option2 Value,Option3 Name,Option3 Value,Variant SKU,Variant Grams,Variant Inventory Tracker,Variant Inventory Qty,Variant Inventory Policy,Variant Fulfillment Service,Variant Price,Variant Compare At Price,Variant Requires Shipping,Variant Taxable,Variant Barcode,Image Src,Image Position,Image Alt Text,Gift Card,SEO Title,SEO Description,Google Shopping / Google Product Category,Google Shopping / Gender,Google Shopping / Age Group,Google Shopping / MPN,Google Shopping / AdWords Grouping,Google Shopping / AdWords Labels,Google Shopping / Condition,Google Shopping / Custom Product,Google Shopping / Custom Label 0,Google Shopping / Custom Label 1,Google Shopping / Custom Label 2,Google Shopping / Custom Label 3,Google Shopping / Custom Label 4,Variant Image,Variant Weight Unit,Variant Tax Code,Cost per item,Collection\n'
with open('db.csv','w') as nuevoArchivo:
    nuevoArchivo.write(encabezado)
    descripcionPrevia = ''

    for rowEx in range(1,hojaExcel.nrows):

        title = str(hojaExcel.cell(rowEx,2).value)
        if ( not title):
            continue
        handle = title 
        handle = unidecode.unidecode(handle)
        handle = handle.replace(' ','-')
        handle = handle.replace(':','')
        body = str(hojaExcel.cell(rowEx,5).value)
        body = body.replace(',',' ').replace("\"",'')
        if not body:
            body = descripcionPrevia
        else:
            descripcionPrevia = body
        vendor = str(hojaExcel.cell(rowEx,3).value)
        tipo = "Libro"
        tags = ""
        published = "TRUE"
        option1Name = "Title"
        option1Value = "Default Title"
        option2Name = ""
        option2Value = ""
        option3Name = ""
        option3Value = ""
        variantSKU = ""
        variantGrams = "400"
        variantInventoryTracker = ""
        variantInventoryQty = "100"
        variantInventoryPolicy = "continue"
        variantFulfillmentService = "manual"
        variantPrice = str(hojaExcel.cell(rowEx,7).value)
        variantCompareAtPrice = str(hojaExcel.cell(rowEx,7).value)
        variantRequiresShipping = "TRUE"
        variantTaxable = "FALSE"
        variantBarcode= str(hojaExcel.cell(rowEx,0).value)
        imageSrc = "http://www.eduvisionmexico.com/site/imgs/portadas/colorin1.png"
        imagePosition = "1"
        imageAltText = ""
        giftCard = "False"
        seoTitle = ""
        seoDescription = ""
        google = ""
        variantImage = ""
        variantWeightUnit = ""
        variantTaxCode =""
        costPerItem = variantPrice 
        collection = str(hojaExcel.cell(rowEx,1).value)
        nuevoArchivo.write(handle + ',' )
        nuevoArchivo.write(title + ',')
        nuevoArchivo.write(body + ',')
        nuevoArchivo.write(vendor + ',')
        nuevoArchivo.write(tipo + ',')
        nuevoArchivo.write(tags + ',')
        nuevoArchivo.write(published + ',')
        nuevoArchivo.write(option1Name + ',')
        nuevoArchivo.write(option1Value + ',')
        nuevoArchivo.write(option2Name + ',')
        nuevoArchivo.write(option2Value + ',')
        nuevoArchivo.write(option3Name + ',')
        nuevoArchivo.write(option3Value + ',')
        nuevoArchivo.write(variantSKU + ',')
        nuevoArchivo.write(variantGrams + ',')
        nuevoArchivo.write(variantInventoryTracker + ',')
        nuevoArchivo.write(variantInventoryQty + ',')
        nuevoArchivo.write(variantInventoryPolicy + ',')
        nuevoArchivo.write(variantFulfillmentService + ',')
        nuevoArchivo.write(variantPrice + ',')
        nuevoArchivo.write(variantCompareAtPrice + ',')
        nuevoArchivo.write(variantRequiresShipping + ',')
        nuevoArchivo.write(variantTaxable + ',')
        nuevoArchivo.write(variantBarcode + ',')
        nuevoArchivo.write(imageSrc + ',')
        nuevoArchivo.write(imagePosition + ',')
        nuevoArchivo.write(imageAltText + ',')
        nuevoArchivo.write(giftCard + ',')
        nuevoArchivo.write(seoTitle + ',')
        nuevoArchivo.write(seoDescription + ',')
        nuevoArchivo.write(google + ',')
        nuevoArchivo.write(google + ',')
        nuevoArchivo.write(google + ',')
        nuevoArchivo.write(google + ',')
        nuevoArchivo.write(google + ',')
        nuevoArchivo.write(google + ',')
        nuevoArchivo.write(google + ',')
        nuevoArchivo.write(google + ',')
        nuevoArchivo.write(google + ',')
        nuevoArchivo.write(google + ',')
        nuevoArchivo.write(google + ',')
        nuevoArchivo.write(google + ',')
        nuevoArchivo.write(google + ',')
        nuevoArchivo.write(variantImage + ',')
        nuevoArchivo.write(variantWeightUnit + ',')
        nuevoArchivo.write(variantTaxCode + ',')
        nuevoArchivo.write(costPerItem + ',')
        nuevoArchivo.write(collection + '\n')